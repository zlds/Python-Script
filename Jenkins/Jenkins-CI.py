# -*- coding: utf-8 -*-
import jenkins

# jenkins url
JENKINS_URL = "http://xxx.com/"

# jenkins user
USER_ID = "user"

# jenkins user id
USER_TOKEN = "id"


class Jenkins_Build:
    def __init__(self, jenkins_url, user_id, user_token):
        self.jenkins_url = jenkins_url
        self.user_id = user_id
        self.user_token = user_token
        self.server = jenkins.Jenkins(JENKINS_URL, USER_ID, USER_TOKEN)

    # 运行job
    def run(self, job_name):
        # 连接Jenkins
        server = jenkins.Jenkins(self.jenkins_url, username=self.user_id, password=self.user_token)
        # 构建项目
        self.server.build_job(job_name)

    def get_result(self, job_name):
        # 找到最后一次构建的序列号
        lastbuildNumber = self.server.get_job_info(job_name)['lastBuild']['number']
        # 查看结果
        result = self.server.get_build_info(job_name, lastbuildNumber)['result']
        print(result)


test = Jenkins_Build(JENKINS_URL, USER_ID, USER_TOKEN)

# test.run('test')
test.get_result('test')
