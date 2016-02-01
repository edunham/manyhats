Many Hats
---------

This is a proof of concept for running
[octohatrack](https://github.com/labhr/octohatrack) on all the repos in an
organization and dumping the results onto GitHub pages.

Setting Up
==========

This deployment copies the terrible pattern that I used with
[orglog](https://github.com/edunham/orglog) and builds the page on TravisCI
then makes Travis push the results to another repo. I don't like giving
poorly-tested bots the credentials to nuke repos of stuff I care about, so
stuff force-pushes elsewhere. 

TravisCI settings
-----------------

Go to https://travis-ci.org/profile/ and click the little button by your fork
of the `manyhats` repo. You might have to hit the 'sync account' button at the
top to make the repo show up. Then click the little `settings` gear by the
repo name, and fill out the necessary environment variables as follows.

The script `out/forcepush.sh` reads some environment variables of the build to
decide what to do. They're configured in the repo's settings in TravisCI.

* `TARGET_REPO` is the name of the repo where you want to push results. Mine
  is set to `rust-manyhats-output`. It should probably be a [newly
  created](https://github.com/new), empty repo. 

* `GH_USER` is the username of the github account or org that owns
  `TARGET_REPO`. 

* `GH_TOKEN` is the string you get when you go to
  https://github.com/settings/tokens/new and create a token with the `repo`
  permission.

Here's how my repo settings page looks after I tell Travis about the
variables: 

![Screenshot of TravisCI repo settings](http://i.imgur.com/Oj5Umui.png)

Nightli.es
----------

To automatically rebuild the page even on days without pushes, log in to
(nightlies)[https://nightli.es/] and flip the switch by the repo's name. Easy!


