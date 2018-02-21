# SLI/SLO Lab

This repository contains the common code for a [Concourse](https://concourse.ci) pipeline
to measure SLIs and verify them against SLOs.

## To implement

1. Clone this repository to your local system
1. Check out the branch associated with your team (`git checkout PCF-PRE<number>`)
1. There will now be two files under the `ci/tasks` directory, `measure-sli` and `verify-slo`.
    Implement these to measure your SLI and SLO according to the `README.md` in that
    branch.
1. Commit that branch's code and push it back to Github. **DO NOT MERGE TO `master`**
1. If you do not already have an SSH key associated with your account, [add one](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

Once those steps are complete, you can set the pipeline in Concourse, as seen below:

*NOTE*: The credentials used during the `fly login` step are the same used to log in to
your Ops Manager instance.

```
$ git checkout master
$ fly -t pal login -n PCF-PRE<number> -c https://concourse.pal.pivotal.io
$ fly -t pal set-pipeline -p sli-lab -c pipeline.yml \
    -v team=PCF-PRE<number> \
    -v team_slack_channel=TODO \
    -v team_private_key="$(cat /path/to/ssh-key)"
$ fly -t pal unpause-pipeline -p sli-lab
```

The pipeline will run every 5 minutes and will alert in Slack if an SLO is violated, or if
the SLI measurement fails.
