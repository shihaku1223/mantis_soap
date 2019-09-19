#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
from mantis_soap.Connector import Connector
from mantis_soap.IssueViewer import IssueViewer
from mantis_soap.Utils import changeIssueProject
from mantis_soap import Utils

from mantisconnect.project import Issue

import datetime
import zeep


if __name__ == '__main__':

    url = "http://osoft-de-c.olympus.co.jp/mantis/ipf3/app/api/soap/mantisconnect.php?wsdl"
    connector = Connector(url, "10079186", "123")
    connector.connect()

    print("Mantis SOAP MC Version:" + connector.getVersion())
    issue = connector.getIssue(41958)
    print(issue)
    viewer = IssueViewer(issue)
    print(viewer.getLastUpdatedTime())
    print(viewer.getProjectName())

    print(viewer.getAttachments())
    print(Utils.addAttachment(connector, 41958, './log.log'))

    '''
    accountType = connector._mc.client.get_type('ns0:AccountData')
    #accountData = accountType(id = 909, name = '10079186', real_name = '王\u3000詩博', email = 'sibo_wang@ot.olympus.co.jp')
    accountData = accountType(name = '10079186')
    '''
    Utils.addNote(connector, 41958, '10079186', 'Hello')

    projectId = connector.getProjectId('CV2KApp窓口')
    print("ProjectId: " + str(projectId))

    try:
        #issues = connector.getProjectIssues(projectId)
        issues = connector.getIssuesByFilter(projectId, 9348, 0, 0)

        print("Issues count:"+ str(len(issues)))
    except zeep.exceptions.TransportError as e:
        print(e.content)
    except zeep.exceptions.XMLSyntaxError as e:
        print(e)
    except zeep.exceptions.Fault as e:
        print(e)

    """
    for issue in issues:
        viewer = IssueViewer(issue)
        print(viewer.getId())
    """
