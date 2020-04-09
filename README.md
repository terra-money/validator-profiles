<img src="img/banner_bg.png" />

## Validator Directory

_NOTE: Validators that have yet to put up a profile have been hidden. Get the full list of validators [here](https://station.terra.money/staking)_

| Moniker          |                                                                             |                                                                                                           |
| ---------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 01node.com       | [Profile](./validators/terravaloper1khfcg09plqw84jxy5e7fj6ag4s2r9wqsgm7k94) | [Station Page](https://station.terra.money/validator/terravaloper1khfcg09plqw84jxy5e7fj6ag4s2r9wqsgm7k94) |
| ATEAM            | [Profile](./validators/terravaloper1tusfpgvjrplqg2fm7wacy4slzjmnzswcfufuvp) | [Station Page](https://station.terra.money/validator/terravaloper1tusfpgvjrplqg2fm7wacy4slzjmnzswcfufuvp) |
| block42          | [Profile](./validators/terravaloper16tc3c9u6yj5uuhru32pvs0pahfwraurpypz7vj) | [Station Page](https://station.terra.money/validator/terravaloper16tc3c9u6yj5uuhru32pvs0pahfwraurpypz7vj) |
| DELIGHT          | [Profile](./validators/terravaloper1fjuvyccn8hfmn5r7wc2t3kwqy09zzp6tyjcf50) | [Station Page](https://station.terra.money/validator/terravaloper1fjuvyccn8hfmn5r7wc2t3kwqy09zzp6tyjcf50) |
| DokiaCapital     | [Profile](./validators/terravaloper1v5hrqlv8dqgzvy0pwzqzg0gxy899rm4kdur03x) | [Station Page](https://station.terra.money/validator/terravaloper1v5hrqlv8dqgzvy0pwzqzg0gxy899rm4kdur03x) |
| Figment Networks | [Profile](./validators/terravaloper15cupwhpnxhgylxa8n4ufyvux05xu864jcv0tsw) | [Station Page](https://station.terra.money/validator/terravaloper15cupwhpnxhgylxa8n4ufyvux05xu864jcv0tsw) |
| FRESHLUNA        | [Profile](./validators/terravaloper1audgfvmgt0js54p3s8kj3r40uwej6vy2tv6rrw) | [Station Page](https://station.terra.money/validator/terravaloper1audgfvmgt0js54p3s8kj3r40uwej6vy2tv6rrw) |
| kytzu            | [Profile](./validators/terravaloper1jyjg55hzsh0f4xymy0kuuan30pp4q75ruqmvyt) | [Station Page](https://station.terra.money/validator/terravaloper1jyjg55hzsh0f4xymy0kuuan30pp4q75ruqmvyt) |
| Staker Space     | [Profile](./validators/terravaloper1pc0gs3n6803x7jqe9m7etegmyx29xw38aaf3u7) | [Station Page](https://station.terra.money/validator/terravaloper1pc0gs3n6803x7jqe9m7etegmyx29xw38aaf3u7) |
| StakeWith.Us     | [Profile](./validators/terravaloper1c9ye54e3pzwm3e0zpdlel6pnavrj9qqvq89r3r) | [Station Page](https://station.terra.money/validator/terravaloper1c9ye54e3pzwm3e0zpdlel6pnavrj9qqvq89r3r) |
| Umbrella         | [Profile](./validators/terravaloper1uhjx34pfsxk9xh34yn8p2w4469uqdz067rqu5g) | [Station Page](https://station.terra.money/validator/terravaloper1uhjx34pfsxk9xh34yn8p2w4469uqdz067rqu5g) |

## Terraform Labs Validators (Do Not Delegate)

| Moniker |                                                                             |                                                                                                           |
| ------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| gazua   | [Profile](./validators/terravaloper1rf9xakxf97a49qa5svsf7yypjswzkutqfhnpn5) | [Station Page](https://station.terra.money/validator/terravaloper1rf9xakxf97a49qa5svsf7yypjswzkutqfhnpn5) |
| Ghost   | [Profile](./validators/terravaloper1rgu3qmm6rllfxlrfk94pgxa0jm37902dynqehm) | [Station Page](https://station.terra.money/validator/terravaloper1rgu3qmm6rllfxlrfk94pgxa0jm37902dynqehm) |
| Goliath | [Profile](./validators/terravaloper163phlen6dn7sp9khhjar2gqqx6kga0ly8d7h9g) | [Station Page](https://station.terra.money/validator/terravaloper163phlen6dn7sp9khhjar2gqqx6kga0ly8d7h9g) |
| Marine  | [Profile](./validators/terravaloper1d3hatwcsvkktgwp3elglw9glca0h42yg6xy4lp) | [Station Page](https://station.terra.money/validator/terravaloper1d3hatwcsvkktgwp3elglw9glca0h42yg6xy4lp) |
| Wraith  | [Profile](./validators/terravaloper1eutun6vh83lmyq0wmyf9vgghvurze2xanl9sq6) | [Station Page](https://station.terra.money/validator/terravaloper1eutun6vh83lmyq0wmyf9vgghvurze2xanl9sq6) |

## What is a Validator Profile?

As a validator, it's not enough to maintain rock-solid, reliable infrastructure -- you also need to market yourself effectively and court delegations from prospecting delegators. Validator Profiles, hosted here on this Github repository give you a platform to give potential delegators and clients a brief introduction on your team, philsophy, architecture and infrastructure, and present your ecosystem contributions. If you need vouching from us, we'll apply a badge for any claims that we can validate.

## How to change your Validator Profile

1. Fork this repository to your own GitHub account.

2. Clone the repo from your own account. Make sure you clone the repository from your account (your fork), NOT the original repo.

```sh
git clone git@github.com:xxxxxx/validator-profiles.git
cd validator-profiles/
```

3. Create a new branch and switch to a new branch by your validator name. For example:

```sh
git checkout -b Wraith-profile
```

4. Copy the template [README.md](./template/README.md) and [JSON Profile](./template/profile.json) into your folder inside `validators/<your-valoper-address>`.

5. Change the contents and add your information as necessary. You can modify anything within your own designated validator folder, including adding image files, new folders, etc.

6. Commit and push the information to your repo.

```sh
git add -A
git commit -m "Edit Wraith profile"
git push origin Wraith-profile
```

7. Under your repo page, click the “New pull request” button. Make a Pull Request with our repository with a summary of changes.

8. We will review your PR as soon as possible. If there is no problem with your PR, we will merge it into our master branch, which will update your Validator Profile. If it is your first time creating a profile, we will add your entry to the [Validator Directory](#validator-directory).
