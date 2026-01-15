from backend.models import User, MenuItem, Order

def test_create_user(test_app):
    app, db = test_app

    user = User(username="testuser", password="hashedpassword")
    db.session.add(user)
    db.session.commit()

    saved_user = User.query.first()

    assert saved_user is not None
    assert saved_user.username == "testuser"


def test_create_menu_item(test_app):
    app, db = test_app

    item = MenuItem(name="Pizza", price=12.5)
    db.session.add(item)
    db.session.commit()

    saved_item = MenuItem.query.first()

    assert saved_item is not None
    assert saved_item.name == "Pizza"
    assert saved_item.price == 12.5


def test_create_order(test_app):
    app, db = test_app

    user = User(username="orderuser", password="123")
    db.session.add(user)
    db.session.commit()

    order = Order(user_id=user.id, status="Pending")
    db.session.add(order)
    db.session.commit()

    saved_order = Order.query.first()

    assert saved_order is not None
    assert saved_order.status == "Pending"
    assert saved_order.user_id == user.id