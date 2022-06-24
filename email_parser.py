import json
import os
import re

# Alert: Ensure script is executed in validator-profiles directory.
run_dir = os.path.join(os.getcwd(), 'validators')
validators_json = {}
errors = {}
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Iterate over validator directories.
for val_address in os.listdir('./validators'):

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
        errors[val_address] = (type(error).__name__, info)
    
    # Add validator directories which didn't include a profile.json file.
    except (FileNotFoundError) as error:
        errors[val_address] = type(error).__name__

    # Create new_validators.json file.
    with open('new_validators.json', 'w') as json_file:
        json.dump(
            validators_json,
            json_file,
            indent=2,
            separators=(',', ': '),
            sort_keys=True
        )
        json_file.write('\n')

# Print relevant errors for exploration.
print(json.dumps(errors, indent=2, sort_keys=True))
