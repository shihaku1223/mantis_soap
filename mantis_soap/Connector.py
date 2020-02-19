#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#from mantisconnect.connector import MantisSoapConnector
from mantisconnect.project import Issue

from suds.client import Client
from zeep import Client as ZeepClient
from zeep import Settings

class SoapClient:
    def __init__(self, url, user, password):
        self._mantis_url = url
        self.client = None
        self.user_name = user
        self.user_passwd = password
        self.version = None

    def connect(self):
        settings = Settings(strict=False, xml_huge_tree=True)
        self.client = ZeepClient(self._mantis_url, settings = settings)

        self.version = self.client.service.mc_version()

class Connector:
    def __init__(self, url, username, password):
        self._mc = SoapClient(url, username, password)
        #self._mc = MantisSoapConnector(url)
        #self._mc.set_user_passwd(username, password)

        # another client for issue_attachment_add
        self._client = Client(url)

    def connect(self):
        self._mc.connect()

    def getVersion(self):
        return self._mc.version

    def getIssue(self, id):
        issue = self._mc.client.service.mc_issue_get(
            self._mc.user_name, self._mc.user_passwd, id)
        return issue

    def getProjectId(self, name):
        project = self._mc.client.service.mc_project_get_id_from_name(
            self._mc.user_name, self._mc.user_passwd, name)

        if project == 0:
            return None
        return project

    def getProjectCategories(self, projectId):

        return self._mc.client.service.mc_project_get_categories(
            self._mc.user_name,
            self._mc.user_passwd,
            projectId)

    def getIssuesByFilter(self, projectId, filter_id, page, per_page):

        return self._mc.client.service.mc_filter_get_issues(
            self._mc.user_name,
            self._mc.user_passwd,
            projectId,
            filter_id,
            page,
            per_page)

    def getIssueAttachment(self, id):
        attachment = self._mc.client.service.mc_issue_attachment_get(
            self._mc.user_name,
            self._mc.user_passwd,
            id)
        return attachment

    def getProjectIssues(self, projectId, page = 0, itemPerPage = 50):
        mc = self._mc

        issues = self._mc.client.service.mc_project_get_issues(
            mc.user_name,
            mc.user_passwd,
            projectId, page, itemPerPage)

        return issues

    def getProjectUsers(self, projectId):
        mc = self._mc

        users = self._mc.client.service.mc_project_get_users(
            mc.user_name,
            mc.user_passwd,
            projectId, 0)
        return users

    def addAttachment(self, issueId, file_name, file_type, base64):
        mc = self._mc

        response = self._client.service.mc_issue_attachment_add(
            mc.user_name,
            mc.user_passwd,
            issueId,
            file_name,
            file_type,
            base64)

        return response

    def addIssue(self, projectId, category,
            summary, description, reporter,
            severity = None):
        mc = self._mc

        issueType = self._mc.client.get_type('ns0:IssueData')
        objType = self._mc.client.get_type('ns0:ObjectRef')

        #status = objType(id = statusId)
        project = objType(id = projectId)
        #statusId = objType(id = statusId)
        issue = issueType(
            project = project,
            category = category,
            summary = summary,
            description = description,
            reporter = reporter)

        response = self._mc.client.service.mc_issue_add(
            mc.user_name,
            mc.user_passwd,
            issue)

        return response


    def deleteIssue(self, issueId):
        mc = self._mc

        response = self._mc.client.service.mc_issue_delete(
            mc.user_name,
            mc.user_passwd,
            issueId)

        return response

    def addNote(self, issueId, accountData, message):
        mc = self._mc

        noteType = self._mc.client.get_type('ns0:IssueNoteData')
        note = noteType(reporter = accountData, text = message)

        response = self._mc.client.service.mc_issue_note_add(
            mc.user_name,
            mc.user_passwd,
            issueId,
            note)

        return response

    def updateIssueSummary(self, originIssue, summary):
        mc = self._mc

        objType = self._mc.client.get_type('ns0:ObjectRef')

        project = objType(id = originIssue['project']['id'])
        category = originIssue['category']

        issueType = self._mc.client.get_type('ns0:IssueData')

        issue = issueType(
            project = project,
            category = category,
            summary = summary,
            description = originIssue['description'],
            reporter = originIssue['reporter'])

        response = self._mc.client.service.mc_issue_update(
            mc.user_name,
            mc.user_passwd,
            originIssue['id'],
            issue)

        return response

    def updateIssueStatus(self, originIssue, statusId):
        mc = self._mc

        objType = self._mc.client.get_type('ns0:ObjectRef')

        status = objType(id = statusId)
        project = objType(id = originIssue['project']['id'])
        category = originIssue['category']

        issueType = self._mc.client.get_type('ns0:IssueData')

        issue = issueType(
            project = project,
            category = category,
            summary = originIssue['summary'],
            description = originIssue['description'],
            reporter = originIssue['reporter'],
            status = status)

        response = self._mc.client.service.mc_issue_update(
            mc.user_name,
            mc.user_passwd,
            originIssue['id'],
            issue)

        return response

    def updateIssueProjectId(self, originIssue, projectId):
        mc = self._mc

        objType = mc.client.get_type('ns0:ObjectRef')
        project = objType(id = projectId)
        category = originIssue['category']
        reporter = originIssue['reporter']

        issueType = self._mc.client.get_type('ns0:IssueData')
        issue = issueType(
            project = project,
            category = category,
            summary = originIssue['summary'],
            description = originIssue['description'],
            reporter = reporter)

        response = mc.client.service.mc_issue_update(
            mc.user_name,
            mc.user_passwd,
            originIssue['id'],
            issue)

        return response
