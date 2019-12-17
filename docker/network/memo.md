

# docker network新規作成
'''
docker network create -d bridge --gateway=192.168.100.254 --subnet=192.168.100.0/24 --ip-range=192.168.100.48/28 test_nw
docker network create -d bridge --gateway=192.168.101.254 --subnet=192.168.101.0/24 --ip-range=192.168.101.48/28 test_nw2
'''

--gateway ゲートウェイを指定する
--subnet ネットワークのサブネットを指定する。CIDR表記で渡す。
--ip-range コンテナに割り当てるIPアドレス帯をCIDR表記で渡す。


# dockerコンテナ作成
'''
docker run -it -d --privileged --name server_100_1 ubuntu:18.04 /bin/bash
docker run -it -d --privileged --name server_100_2 ubuntu:18.04 /bin/bash
docker run -it -d --privileged --name server_101_1 ubuntu:18.04 /bin/bash
docker run -it -d --privileged --name server_101_2 ubuntu:18.04 /bin/bash
'''


# dockerコンテナにnetwork紐付け
'''
docker network connect {ネットワーク名} {コンテナ名} 
docker network connect test_nw network_server_100_1_1
docker network connect test_nw network_server_100_2_1
docker network connect test_nw2 network_server_101_1_1
docker network connect test_nw2 network_server_101_2_1


'''




