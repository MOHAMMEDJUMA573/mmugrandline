from market import app, db
from market.models import Item
with app.app_context():
    from market.models import Item
    from market import db

    item1 = Item(name="Smart Watch", price=150, barcode="SW1234567890", description="Stylish smart watch with health tracking.")
    item2 = Item(name="Gaming Mouse", price=70, barcode="GM1234567891", description="High DPI RGB gaming mouse.")
    item3 = Item(name="Bluetooth Speaker", price=100, barcode="BS1234567892", description="Portable speaker with powerful bass.")
    item4 = Item(name="LED Monitor", price=300, barcode="LM1234567893", description="24-inch Full HD monitor.")
    item5 = Item(name="USB-C Hub", price=45, barcode="UH1234567894", description="Multiport USB-C hub with HDMI.")
    item6 = Item(name="Mechanical Keyboard", price=120, barcode="MK1234567895", description="RGB mechanical keyboard with blue switches.")
    item7 = Item(name="Wireless Charger", price=40, barcode="WC1234567896", description="Fast wireless charger for smartphones.")
    item8 = Item(name="Noise Cancelling Headphones", price=250, barcode="NC1234567897", description="Over-ear headphones with ANC.")
    item9 = Item(name="External SSD", price=180, barcode="ES1234567898", description="1TB portable SSD with USB 3.2.")
    item10 = Item(name="Fitness Tracker", price=90, barcode="FT1234567899", description="Fitness band with heart rate monitoring.")
    item11 = Item(name="Smartphone Tripod", price=35, barcode="TP1234567810", description="Flexible tripod stand for smartphones.")
    item12 = Item(name="Webcam 1080p", price=80, barcode="WC1234567811", description="HD webcam with built-in mic.")
    item13 = Item(name="Laptop Stand", price=50, barcode="LS1234567812", description="Adjustable aluminum laptop stand.")
    item14 = Item(name="Portable Projector", price=320, barcode="PP1234567813", description="Mini projector for home theater.")
    item15 = Item(name="Action Camera", price=200, barcode="AC1234567814", description="4K waterproof action camera.")
    item16 = Item(name="Wireless Earbuds", price=110, barcode="WE1234567815", description="Bluetooth earbuds with charging case.")
    item17 = Item(name="Gaming Chair", price=450, barcode="GC1234567816", description="Ergonomic chair for gaming and office.")
    item18 = Item(name="Drone", price=600, barcode="DR1234567817", description="Quadcopter drone with HD camera.")
    item19 = Item(name="Electric Toothbrush", price=60, barcode="ET1234567818", description="Rechargeable toothbrush with timers.")
    item20 = Item(name="Smart Lamp", price=70, barcode="SL1234567819", description="WiFi-enabled smart LED lamp.")

    db.session.add_all([
        item1, item2, item3, item4, item5,
        item6, item7, item8, item9, item10,
        item11, item12, item13, item14, item15,
        item16, item17, item18, item19, item20
    ])
    db.session.commit()
