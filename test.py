#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mantis.Connector import Connector
from mantis.IssueViewer import IssueViewer
from mantis.Utils import changeIssueProject

from mantisconnect.project import Issue

import datetime


if __name__ == '__main__':

    url = "http://osoft-de-c.olympus.co.jp/mantis/ipf3/app/api/soap/mantisconnect.php?wsdl"
    connector = Connector(url, "10079186", "vp5QmS1223")
    connector.connect()

    print("Mantis SOAP MC Version:" + connector.getVersion())
    issue = connector.getIssue(30123)
    viewer = IssueViewer(issue)
    print(viewer.getLastUpdatedTime())
    print(viewer.getProjectName())

    projectId = connector.getProjectId('CV2K_App')
    print("ProjectId: " + str(projectId))

    issues = connector.getProjectIssues(projectId)
    print("Issues count:"+ str(len(issues)))

    #projectId = connector.getProjectId('sandbox_integ')
    projectId = connector.getProjectId('TEST')
    print(projectId)
    changeIssueProject(connector, 30123, projectId)
