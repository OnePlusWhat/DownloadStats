### DownloadStats

A simple python utility to grab the download counts for all releases of a particular 
repository


# Usage

Usage is as simple as `./stats.py <github_username> <name_of_repository>`

For example, here's the stats for [kubernetes](https://github.com/kubernetes/kubernetes)

```
( msfjarvis@jarvisbox | 23:33 ) ~/git-repos/DownloadStats (master)  $ ./stats.py kubernetes kubernetes
kubernetes.tar.gz, tag: v1.7.6, created at 2017-09-14T12:19:37Z
Downloaded 277 times

kubernetes.tar.gz, tag: v1.6.10, created at 2017-09-13T22:06:09Z
Downloaded 102 times

kubernetes.tar.gz, tag: v1.8.0-beta.1, created at 2017-09-08T02:47:52Z
Downloaded 202 times

kubernetes.tar.gz, tag: v1.7.5, created at 2017-08-31T13:40:17Z
Downloaded 1680 times

kubernetes.tar.gz, tag: v1.8.0-alpha.3, created at 2017-08-24T00:01:20Z
Downloaded 237 times

kubernetes.tar.gz, tag: v1.6.9, created at 2017-08-23T20:02:09Z
Downloaded 616 times

kubernetes.tar.gz, tag: v1.7.4, created at 2017-08-17T17:28:11Z
Downloaded 1328 times

kubernetes.tar.gz, tag: v1.6.8, created at 2017-08-03T20:20:13Z
Downloaded 698 times

kubernetes.tar.gz, tag: v1.7.3, created at 2017-08-03T11:34:22Z
Downloaded 1577 times

kubernetes.tar.gz, tag: v1.7.2, created at 2017-07-21T12:34:53Z
Downloaded 2006 times

kubernetes.tar.gz, tag: v1.7.1, created at 2017-07-14T04:23:04Z
Downloaded 1127 times

kubernetes.tar.gz, tag: v1.8.0-alpha.2, created at 2017-07-13T03:08:08Z
Downloaded 153 times

kubernetes.tar.gz, tag: v1.6.7, created at 2017-07-05T19:12:36Z
Downloaded 2063 times

kubernetes.tar.gz, tag: v1.7.0, created at 2017-06-30T06:35:32Z
Downloaded 1543 times

kubernetes.tar.gz, tag: v1.7.0-rc.1, created at 2017-06-24T22:29:04Z
Downloaded 246 times

kubernetes.tar.gz, tag: v1.8.0-alpha.1, created at 2017-06-20T00:13:55Z
Downloaded 154 times

kubernetes.tar.gz, tag: v1.6.6, created at 2017-06-16T20:56:00Z
Downloaded 2026 times

kubernetes.tar.gz, tag: v1.7.0-beta.2, created at 2017-06-15T18:55:40Z
Downloaded 163 times

kubernetes.tar.gz, tag: v1.6.5, created at 2017-06-14T22:26:16Z
Downloaded 520 times

kubernetes.tar.gz, tag: v1.7.0-beta.1, created at 2017-06-08T03:22:36Z
Downloaded 228 times

kubernetes.tar.gz, tag: v1.6.4, created at 2017-05-19T19:59:23Z
Downloaded 3662 times

kubernetes.tar.gz, tag: v1.7.0-alpha.4, created at 2017-05-18T19:30:48Z
Downloaded 124 times

kubernetes.tar.gz, tag: v1.6.3, created at 2017-05-10T18:26:37Z
Downloaded 1942 times

kubernetes.tar.gz, tag: v1.7.0-alpha.3, created at 2017-05-05T18:23:36Z
Downloaded 186 times

kubernetes.tar.gz, tag: v1.5.7, created at 2017-04-27T12:28:20Z
Downloaded 1779 times

kubernetes.tar.gz, tag: v1.4.12, created at 2017-04-20T21:46:08Z
Downloaded 3303 times

kubernetes.tar.gz, tag: v1.7.0-alpha.2, created at 2017-04-20T16:40:38Z
Downloaded 117 times

kubernetes.tar.gz, tag: v1.6.2, created at 2017-04-19T22:58:23Z
Downloaded 3115 times

kubernetes.tar.gz, tag: v1.7.0-alpha.1, created at 2017-04-06T21:06:20Z
Downloaded 593 times

kubernetes.tar.gz, tag: v1.6.1, created at 2017-04-03T22:54:55Z
Downloaded 4843 times
```
