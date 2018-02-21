# Implementing your SLI and SLO measurements / verifications

Important things to know:
1. These commands will run in a docker `ubuntu:latest` image. Anything you can install
    on Ubuntu, you can install here.
1. This script runs every five minutes, so make sure that whatever you do doesn't take too
    long to run!
1. It's very common to implement these scripts in Bash, and it's recommended you do so here.
    However, if you're more comfortable in something like Python or Ruby, consider using a Bash
    script to install the necessary libraries and just calling a helper script that can live in this
    branch. In your bash script, it would be available in the `team-source` subdirectory of the
    directory the script starts in.

## Implementing `measure-sli`

This script should hit the URL of an app (see note below) you choose to measure, and measure the SLI(s)
that you've chosen. Those may be success rates, average latency, etc. In general, "point in time"
SLI measurements are not very useful but given the constraints of the class, it will give
you an idea what needs to be done. You can use your script to call the URL multiple times
and average things, if you'd like.

*Tip!* `curl` is not installed on the base image, but can be.
*Tip!* Use the `-w` flag with `curl` to get information back. For example,
`curl -w 'HTTP Code: %{http_code}, Total Time: %{time_total}' -s -o /dev/null http://www.google.com`

The "results" of your SLI measurement, however you want to define that, need to go
into a file in the `sli-value` directory in the container. That directory will exist already.

If you encounter an error measuring your SLI, you should put an appropriate message into
a file `sli-value/error` and exit your script with a non-zero exit code (`exit 1`, for example).
This will tell Concourse that something is wrong and will notify you via Slack.

## Implementing `verify-slo`

Once you have measured your SLI, it's time to compare it to your defined SLOs. You will
have access to the `sli-value` directory from the previous step. You should use the file
you created in that step to get the values you measured and compare them against some
values you have determined.

If SLOs are violated, you should put an appropriately descriptive message into a file called
`slo-failure/message` (the `slo-failure` directory will already exist), and exit with a
non-zero code. This will tell Concourse to notify you via Slack.

### Note about using apps

You can use any app you choose. If you wish to use an app that can simulate latency and
response errors, a sample app that is appropriate for running on Pivotal Cloud Foundry
exists [here](https://github.com/jghiloni/sample-error-app).
