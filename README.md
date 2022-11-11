## Docker Version確認

 `docker version`
 
## Docker コンテナイメージのビルド 

`docker image build -t flask .`

## コンテナ起動

`docker run -p 5000:80 -v ${PWD}/app:/app -d flask`

## 注意点

`flask_testのパス直下でコマンド実行`