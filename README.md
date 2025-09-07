# **Python テストサンプル集**

このリポジトリは、Pythonにおけるユニットテストの様々な側面を示すためのサンプルコードとテストファイルを含んでいます。unittestおよびpytestフレームワークを使用したテストの書き方、そしてモックオブジェクトを使った依存関係のシミュレーション方法について学ぶことができます。

## **含まれるファイル**

* foo.py / footest.py: unittest を使った基本的な関数のテスト例です。  
* inventory.py / inventorytest.py: 在庫管理クラスと、pytest を使ったその振る舞いをテストする例です。  
* order.py / ordertest.py: 注文処理クラスと、unittest.mock.Mock を使って外部サービス（支払い処理）をシミュレートするテスト例です。  
* finaltest.py: 注文と在庫の更新という、複数のクラス間の連携をテストする統合テスト例です。

## **テストの実行方法**

### **前提条件**

このプロジェクトのテストを実行するには、pytestをインストールする必要があります。

pip install pytest

### **テストの実行**

プロジェクトのルートディレクトリから、以下のコマンドを実行してすべてのテストを実行できます。

pytest

## **サンプルコードの解説**

### **foo.py と footest.py**

* foo.py には、2つの整数を加算するシンプルな関数 add\_int が定義されています。  
* footest.py では、Python標準ライブラリの unittest.TestCase を継承したクラスを使って、add\_int が正しく機能するかを検証しています。

### **inventory.py と inventorytest.py**

* inventory.py の Inventory クラスは、商品の在庫を管理します。  
* inventorytest.py では pytest の assert ステートメントを使って、在庫が正常に更新されるケースと、在庫不足で更新が失敗するケースをテストしています。

### **order.py と ordertest.py**

* order.py の Order クラスは、注文の支払い処理ロジックを含んでいます。  
* ordertest.py は、unittest.mock.Mock を利用して、実際に外部の支払いシステムと通信することなく、PaymentProcessor クラスの動作をシミュレートしています。これにより、支払い成功時と失敗時の両方のシナリオを簡単にテストできます。

### **finaltest.py**

* このファイルは、Order と Inventory という独立したコンポーネントが連携して動作するシナリオをテストします。  
* 支払い処理をモック化しつつ、注文が正常に処理された後に在庫が期待通りに減少するかを検証しています。これは、より複雑なシステムの**統合テスト**の書き方を示す良い例です。
