---
Moniker: lambdacore
Validator: terravaloper1mgdsc0get3w984h03a02zy6gmg3kgqtfqs3tky
Email: info@lambdacore.finance
Discord: @russel-vivier
---

# 🚀 Lambda Core

![](./lambda-title.png)

[We are a team](http://lambdacore.finance/) of experienced software developers and IT infrastructure administrators and strong proponents of automation and self-governance in all aspects. That's why we work in the area of cryptocurrencies and that's how we build our systems: no manual intervention is ever required.

## Our Architecture

Lambda Core validator automatically scales with the growth of the network, has strong lines of defense and can automatically recover in case of failure, be it due to hardware failure or an external attack.

Lambda Core infrastructure runs on a total of four full nodes: three sentry nodes and a validator node. Sentry nodes shield the validator node from the Internet: a hardware firewall is configured to drop any incoming connections to the Validator node that do not come from one of the sentry nodes. Even administrative SSH access to the validator node is only possible through a chain of three SSH bastions, each only accessible from the previous one.

Sentry nodes are "disposable": in case of a failure or an attack, a block storage device containing the blockchain data is **automatically** detached from the Sentry server in question, the server is torn down and re-created afresh, with new public IP, and the block storage device is then re-attached back to it. The whole process of refreshing a node like this takes about 6-7 minutes, and then 1-2 minutes are needed for the `terrad` to start and catch up to the blocks that were missed during the tear-down/spin-up.

After **automatic** re-provisioning of the Sentry node, the watchdog system updates the internal DNS records for service discovery and firewall rules, so the Validator node can still access the new sentry node without needing to update validator config and restart the validator process (and thus miss blocks). Sentry nodes **automatically** go through this process after random intervals of time not exceeding 96 hours. This is necessary to ensure that our protection mechanisms are operational in case we need to re-provision the Validator node.

Validator node will automatically go through a similar process in case of failure or attack and thus will never miss more than 10 minutes worth of new blocks, even in case of a heavy attack.

## Ecosystem Contributions

We are working on a Validator status dashboard to show realtime updates to our delegators. We are also looking into ways of compacting the Terra blockchain data, so that it is easier and cheaper for everyone to run a full node, which would increase reliability of the ecosystem.

## Contact Us

Have questions? You can reach us:

- Email: [`info@lambdacore.finance`](mailto:info@lambdacore.finance)
- Discord: `@russel-vivier` (find us in [Terra](https://discord.gg/ftBEBurm) and [Terra Validators](https://discord.gg/TxsE6ryh) discord rooms)
- Website: http://lambdacore.finance/
