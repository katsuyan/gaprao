# 高度情報演習1B 授業情報共有サービス(仮)

高度情報演習1B
授業情報共有サービス

### ローカル
#### インストール
* VirtualBox
* vagrant

#### サーバーセットアップ
```
git clone git@bitbucket.org:sstty/gaprao.git
vagrant up
vagnrat ssh
cd /home/gaprao
python manage migrate
uwsgi /home/gaprao/uwsgi.ini
```


### 本番
デプロイスクリプトを用意していないので、以下の作業をしてください。
#### 作業
* /home/いかにgapraoのgaprao/gapraoを設置
* gaprao_nginx.confないのIPアドレスを適宜変更
* provision.shを実行

#### サーバセットアップ
```
cd /home/gaprao
python manage migrate
uwsgi /home/gaprao/uwsgi.ini
```
