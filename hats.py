#! /usr/bin/env python2

"""
This script wraps octohatrack to provide contributor stats across an entire
GitHub organization, rather than just for one repo.
"""
import os
import sys
import urllib3
from github import Github, GithubException
from html_boilerplate import *
from octohatrack.helpers import *
limit = 0 #hatrack takes a limit val


def get_user_html(user, repo):
    url = "https://github.com/%s/issues?q=involves:%s" % (repo, user["user_name"])
    html = ("<div><a href='%s'><img src='%s' width='128' alt='%s'></a><div>%s</div></div>\n" % (url, user["avatar"], user["user_name"], user['name']))
    return html


def get_html_hats(repo):
    print "Getting hats for %s" % repo
    hats = "<h1>Contributions for %s</h1>\n" % repo
    coders = get_code_contributors(repo)
    commenters = get_code_commentors(repo, limit)
    code_contributors = sorted(coders, key=lambda k: k['user_name'].lower())
    code_commentors = sorted(commenters, key=lambda k: k['user_name'].lower())
    noncode = [u for u in code_commentors if u not in code_contributors]
    if len(noncode) > 0:
        hats += "<h2> Non-Code contributors</h2>\n"
        hats += '<div class="contributors">\n'
        for user in noncode:            
            hats += get_user_html(user, repo)
        hats += '</div>'
    else:
        hats += "Found no non-code contributors for %s.\n" % repo
    if len(code_contributors) > 0:
        hats += "<h2> Code contributors</h2>\n"
        hats += '<div class="contributors">\n'
        for user in code_contributors:
            hats += get_user_html(user, repo)
        hats += "</div>\n" 
    else:
        hats += "Found no code contributors for %s.\n" % repo
    return hats
    
def main():
    g = Github(os.environ['GH_TOKEN'])
    orgs = sys.argv[1:]
    page = open("index.html", 'w')
    page.write(preamble)
    print orgs
    for o in orgs:
        repos = g.get_user(o).get_repos()
        for r in repos:
            hats = get_html_hats(o + '/' + r.name).encode('utf8')
            page.write(hats)
            page.write(betweenrepos)
        page.write(betweenorgs)
    page.write(postamble)
    page.close()

if __name__ == "__main__":
    main()
