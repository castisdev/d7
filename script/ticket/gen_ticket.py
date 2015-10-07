#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getpass import getpass
import xmlrpc.client

###################################
# 여기를 수정해 주세요
trac_url = '172.16.33.2:8080/trac'
name = '윤기선'
###################################


def gen_ticket(server, round, summary, site, project):
    desc = '%s\n- 주초시작, 완료예정\n- 고객사: %s\n- 프로젝트: %s\n' % (round, site, project)
    ret = server.ticket.create(summary, desc,
                               {'component': '기타', 'type': '형상개선',
                                'due_date': round, 'reporter': name,
                                'exp_duedate': round, 'owner': name,
                                'priority': '0.3'})
    print('ticket #%d [%s] created.' %
          (ret, server.ticket.get(ret)[3]['summary']))


def gen_vacation_ticket(server, round, summary):
    desc = '%s\n- 주초시작, 완료예정\n- 고객사: \n- 프로젝트: \n' % (round)
    s = '%s (%s)' % (summary, name)
    ret = server.ticket.create(s, desc,
                               {'component': '기본 업무', 'type': '휴가',
                                'due_date': round, 'reporter': name,
                                'exp_duedate': round, 'owner': name,
                                'priority': '0.3'})
    print('ticket #%d [%s] created.' %
          (ret, server.ticket.get(ret)[3]['summary']))


def main():
    trac_id = input('trac username:')
    trac_pass = getpass('trac password:')
    trac_rpc_url = 'http://%s:%s@%s/login/rpc' % (trac_id, trac_pass, trac_url)
    server = xmlrpc.client.ServerProxy(trac_rpc_url)

    ###################################
    # 여기를 적절하게 수정해 주세요
    gen_vacation_ticket(server, '2015.17R(0817)', '오후반차 2015.08.26')
    # gen_vacation_ticket(server, '2015.20R(0930)', '연차 2015.10.02')
    # gen_ticket(server,
    #            '2015.20R(0930)',
    #            'GoyoProbe 퍼지로그 수집기능 제거, main 함수 예외 처리',
    #            'KT',
    #            '통합포털UI')
    ###################################

if __name__ == '__main__':
    main()
