import json
import os
import re

# Alert: Ensure script is executed in validator-profiles directory.
RUN_DIR = os.path.join(os.getcwd(), 'validators')


def parse_emails(run_dir=RUN_DIR):
    """
    Parses contact emails from validator 'profile.json' files.

    Args:
        run_dir: Path to local 'validators-profiles/validators' directory.

    Returns:
        validators_json: Dictionary with validator address, email
            key-value pairs.

        errors_json: Dictionary with validator address, error summary
            key-value pairs
    """

    email_regex = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    validators_json = {}
    errors_json = {}

    # Iterate over validator directories.
    for val_address in os.listdir(run_dir):

        # Skip over non-Terra address directories.
        if val_address[0:5] != 'terra':
            continue

        # Set directory for validator's profile.json file.
        profile_dir = os.path.join(run_dir, val_address, 'profile.json')

        # Attempt to extract email from profile.
        try:
            with open(profile_dir) as json_file:
                info = json.load(json_file)
                email_check = all([re.fullmatch(email_regex, email) for email in info['contact']['email']]) or \
                    re.fullmatch(email_regex, info['contact']['email'])
                if info['contact']['email'] and email_check:
                    validators_json[val_address] = info['contact']['email']
                else:
                    raise(ValueError)

        # Add json, key and value errors with corresponding profile.json contents for analysis.
        except (json.decoder.JSONDecodeError, KeyError, ValueError) as error:
            errors_json[val_address] = (type(error).__name__, info)

        # Add validator directories which didn't include a profile.json file.
        except (FileNotFoundError) as error:
            errors_json[val_address] = type(error).__name__

    return validators_json, errors_json


def generate_validators(validators_json):
    """
    Generates new 'validators.json' file with updated validator profile
    additions, deletions or modifications.

    Args:
        validators_json: Dictionary with validator address, email
            key-value pairs.

    Generates:
        validators.json: Stylized JSON file containing validators_json data.
    """

    # Create new validators.json file.
    with open('validators.json', 'w') as json_file:
        json.dump(
            validators_json,
            json_file,
            indent=2,
            separators=(',', ': '),
            sort_keys=True
        )
        json_file.write('\n')


def print_errors(errors_json):
    """
    Prints out errors_json which contains validator addresses with
    corresponding errors that occured during email parsing.

    Args:
        errors_json: Dictionary with validator address, error summary
            key-value pairs
    """

    # Print relevant email parse errors for exploration.
    print(json.dumps(errors_json, indent=2, sort_keys=True))


if __name__ == '__main__':
    validators_json, errors_json = parse_emails()
    generate_validators(validators_json)
    print_errors(errors_json)
