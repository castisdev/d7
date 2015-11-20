#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getpass import getpass
import xmlrpc.client

###################################
# 여기를 수정해 주세요
trac_url = '172.16.33.2:8080/trac'
name = '장세연'
###################################


def gen_ticket(server, round, summary, site, project):
    desc = '%s\n- 주초시작, 완료예정\n- 고객사: %s\n- 프로젝트: %s\n' % (round, site, project)
    if site and project:
        project_name = '(' + site + ')_' + project
    else:
        project_name = ''
    ret = server.ticket.create(summary, desc,
                               {'component': '기타', 'type': '형상개선',
                                'due_date': round, 'reporter': name,
                                'exp_duedate': round, 'owner': name,
                                'priority': '0.3',
                                'project_name': project_name})
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
    # gen_vacation_ticket(server, '2015.4R(0216)', '연차 2015.02.17')
    # gen_vacation_ticket(server, '2015.6R(0316)', '오전 공가(민방위) 2015.03.19')
    # gen_vacation_ticket(server, '2015.6R(0316)', '오후 반차 2015.03.19')
    # gen_vacation_ticket(server, '2015.8R(0413)', '연차 2015.04.13')
    # gen_vacation_ticket(server, '2015.11R(0526)', '오후 반차 2015.05.28')
    # gen_vacation_ticket(server, '2015.14R(0706)', '연차 2015.07.07')
    # gen_vacation_ticket(server, '2015.18R(0831)', '연차 2015.09.04')

    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '팀 주간 회의',
    #     '',
    #     '')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '팀 관리 업무',
    #     '',
    #     '')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '웜홀 일일 회의',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '웜홀 2차 구체화',
    #     'KT',
    #     '공통')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] 웜홀 2차 기술 자료 분석',
    #     'KT',
    #     '공통')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] 중앙 gsdm 에서 available-resource 계산 시에 sink 개수가 source 자원 개산에 반영되지 않는 버그 수정',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] ads 채널 생성 실패 시에 기존 채널 삭제 후 재생성',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] cache 타입은 source location 으로 사용하지 못하도록 하던 제한 제거',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] 지역 GSDM 연결 시에 local address 로 bind 하는 기능 추가',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] 시퀀스 다이어그램 업데이트',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.21R(1012)',
    #     '[GSDM] dist_group 별로 source interface 지정 기능 추가',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    #
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '팀 주간 회의',
    #     '',
    #     '')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '팀 관리 업무',
    #     '',
    #     '')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '웜홀 일일 회의',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '삼성 오픈소스 컨퍼런스 참석',
    #     '',
    #     '')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '소프트웨어 개발 랩 이슈 회의',
    #     '',
    #     '')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '웜홀 2차 구체화',
    #     'KT',
    #     '공통')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 지역 gsdm 에서 source 의 ip 와 멀티캐스트 채널 풀 매핑',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 중복 입수 방지',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 일반/광고 파일 초기 배포 시에 장애 노드 제외',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] websocket 재연결 시에 local address bind 하지 않는 버그 수정',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 전체 파일 삭제 시에 실제로 파일 삭제 수행 후에 응답',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] analyzer 순위표를 얻는데 실패한 경우 다음 재배포 주기를 기다리지 않고 재시도',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 초기배포/수동배포일 때 배포 시작 후 정상 종료 시에 copy_info 가 삭제되는 버그 수정',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 수동 배포 중복 방지',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 입수/재배포 목록 이력 관리',
    #     'KT',
    #     '미디어웜홀/통합운영포털')
    # gen_ticket(server,
    #     '2015.22R(1026)',
    #     '[GSDM] 입수/재배포 목록 개수/시간으로 유지하는 기능 추가',
    #     'KT',
    #     '미디어웜홀/통합운영포털')

    ###################################

if __name__ == '__main__':
    main()
