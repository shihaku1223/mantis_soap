#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from mantis.Connector import Connector
from mantis.IssueViewer import IssueViewer

from mantisconnect.project import Issue

import datetime


if __name__ == '__main__':

    url = "http://osoft-de-c.olympus.co.jp/mantis/ipf3/app/api/soap/mantisconnect.php?wsdl"
    connector = Connector(url, "10079186", "vp5QmS1223")
    connector.connect()

    print("Mantis SOAP MC Version:" + connector.getVersion())
    issue = connector.getIssue(31286)
    viewer = IssueViewer(issue)
    print(viewer.getLastUpdatedTime())

    projectId = connector.getProjectId('CV2K_App')
    print("ProjectId: " + str(projectId))

    issues = connector.getProjectIssues(projectId)
    print("Issues count:"+ str(len(issues)))
