import pytest
from unittest.mock import Mock
from order import Order
from payment_processor import PaymentProcessor

# 测试订单创建
def test_order_creation():
    order = Order(order_id=1, amount=100)
    assert order.order_id == 1
    assert order.amount == 100
    assert order.status == 'created'

# 测试支付成功
def test_order_payment_success():
    # 使用Mock来模拟PaymentProcessor的行为
    mock_payment_processor = Mock(spec=PaymentProcessor)
    mock_payment_processor.process_payment.return_value = True

    order = Order(order_id=1, amount=100)
    success = order.process_payment(mock_payment_processor)
    assert success is True
    assert order.status == 'paid'

# 测试支付失败
def test_order_payment_failure():
    mock_payment_processor = Mock(spec=PaymentProcessor)
    mock_payment_processor.process_payment.return_value = False

    order = Order(order_id=1, amount=100)
    success = order.process_payment(mock_payment_processor)
    assert success is False
    assert order.status == 'created'
