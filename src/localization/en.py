# Misc buttons
try_again = "Try again."
skip = "⏭ Skip"
back = "🔙 Back"
tick = "✅"
cross = "❌"
yes = "✅ Yes"
no = "❌ No"
enabled = "✅ Enabled"
disabled = "❌ Disabled"
error = "An error occurred!"
or_press_back = "or press the \"Back\" button."
or_press_skip = "or press the \"Skip\" button."
hide = "🙈 Hide"
show = "🐵 Show"
delete = "❌ Delete"
reset = "❌ Reset"
no_permission = "You don't have permission to perform this command!"
unknown_command = "Cannot understand the command :("
too_many_categories = "Too many categories!"
unknown_call_stop_state = "The bot is waiting for your input, but you didn't enter anything. To exit the data input mode, press the button below."
state_cancelled = "You cancelled the operation."
unknown_error = "An unknown error occurred!"

# main markup
admin_panel = "🔴 Admin panel"
faq = "ℹ️ FAQ"
profile = "📁 Profile"
catalogue = "🗄️ Catalog"
cart = "🛒 Cart"
support_menu = "☎ Support menu"

# Cart
payment_method = "💳 Payment method"
choose_payment_method = "Choose a payment method:"
def format_delivery(delivery_price: int) -> str:
    return f"🚚 Delivery: {delivery_price} rub."
delivery = "🚚 Delivery"
self_pickup = "🖐️ Self-pickup"
cart_empty = "Your cart is empty!"
def cart_total_price(price: float, currency_sym: str) -> str:
    return f"🛒 Total price: {price:.2f} {currency_sym}"

# Admin panel tabs
item_management = "📦 Item management"
no_categories = "Create at least one category before creating an item!"
user_management = "🧍 User management"
category_management = "📁 Categories"
stats = "📈 Statistics"
settings = "⚙ Settings"

# Main settings
language = "🌐 Language"
choose_a_language = f"Choose a language {or_press_skip}:"
language_was_set = "Language was successfully changed! Restart the bot to apply the changes."
english = "🇬🇧 English"
russian = "🇷🇺 Russian"
input_greeting = "Format: \n\"%s\" - user nickname\n\nEnter a greeting message:"
greeting_was_set = "The greeting message was successfully changed!"

greeting = "👋 Greeting"

# FAQ
contacts = "📞 Contacts"
refund_policy = "🎫 Refund policy"

# Profile
my_orders = "📂 My orders"
cancel_order = "❌ Cancel order"
restore_order = "✅ Restore order"
my_support_tickets = "🙋 My support tickets"
enable_notif = "🔔 Enable order notifications"
disable_notif = "🔕 Disable order notifications"

# Catalogue / Item / Cart
search = "🔍 Search"
add_to_cart = "🛒 Add to cart"
not_in_stock = "❌ Out of stock"
cart_is_empty = "Cart is empty."
category_is_empty = "Category is empty."
textpickup = "✅Self-pickup"
def delivery_on(price): return f"✅ Delivery - {price}rub."
def delivery_off(price): return f"❌ Delivery - {price}rub."
cart_checkout = "Checkout"
clear_cart = "Clear cart"
status_processing = "Processing"
status_delivery = "Waiting for delivery"
status_done = "Done"
status_cancelled = "Cancelled"
def item(item):
    stock = "on order" if item.is_custom else f"{item.amount}"
    return f"{item.name}\n{item.price:.2f} rub.\nIn stock: {stock}\n{item.description}"

# Category management
add_category = "🛍️ Add category"
edit_category = "✏️ Edit category"
input_category_name = f"Enter category name {or_press_back}"
set_parent_category = f"📁 Select parent category {or_press_skip}"
category_created = "Category successfully created."
def format_category(category_id, category_name, category_parent_id, category_parent_name):
    return f"Category: [{category_id}]{category_name}\nParent category: {f'[{category_parent_id}]{category_parent_name}' if category_parent_id else 'None'}"
edit_parent_category = "📁 Edit parent category"
choose_a_category_to_edit = "Choose a category to edit:"
confirm_delete_category = "Are you sure you want to delete the category?"
category_deleted = "Category successfully deleted."

# Item management
def format_editItemsCategory_text(category_name: str) -> str:
    return f"Choose an item to edit in the {category_name} category:"
add_item = "🗃️ Add item"
edit_item = "✏️ Edit item"

edit_name = "📋 Edit name"
input_item_name = f"Enter item name {or_press_back}"

choose_category = "📁 Choose category"
select_item_category = f"📁 Select item category {or_press_back}"
edit_category = "✏️ Edit category"

input_item_description = f"Enter item description {or_press_back}"
edit_description = "📝 Edit description"

input_item_price = f"Enter item price {or_press_back}"
edit_price = "💰 Edit price"
price_must_be_number = "Price must be a number."

send_item_images = f"🖼️ Send item image {or_press_skip}"
send_item_changed_images = f"🖼️ Send item image {or_press_back}"
delete_image = "❌ Delete image"
edit_image = "🖼️ Edit image"


confirm_delete_item = "Are you sure you want to delete the item?"
item_was_deleted = "Item successfully deleted."
change_desc = "📝 Edit description"
change_price = "🏷️ Edit price"
change_item_cat = "🛍️ Edit category"
change_stock = "📦 Edit stock"
def format_confirm_item(name: str, description: str, category_id: int, price: float, images: list[str]) -> str:
    return f"Item: {name}\nDescription: {description}\nCategory: {category_id}\nPrice: {price}\nImage IDs: {images}\n\nAre you sure you want to create this item?"
item_added = "Item successfully added."

# User management
user_does_not_exist = "User not found. {try_again}"
def format_user_profile(id: int, username: str, registration_date: str, is_admin: bool, is_manager: bool) -> str:
    role = "User"
    if is_admin:
        role = "Administrator"
    elif is_manager:
        role = "Manager"
    return f"ID: {id}\nName: {username}\nRegistration date: {registration_date}\nRole: {role}"
invalid_user_id = "Invalid user ID. {try_again}"

user_profile = "📁User profile"
input_user_id = f"Enter user ID {or_press_back}"
notify_everyone = "🔔Notify all users"
input_notification = f"Enter notification text {or_press_back}"
def confirm_notification(text: str) -> str:
    return f"Are you sure you want to send this notification?\nText:\n{text}"
def notification_sent(done_users: int, total_users: int) -> str:
    return f"Notification successfully sent to {done_users}/{total_users} users."
orders = "📁 Orders"
remove_manager_role = "👨‍💼 Remove manager role"
add_manager_role = "👨‍💼 Add manager role"
remove_admin_role = "🔴 Remove admin role"
add_admin_role = "🔴 Add admin role"
def change_order_status(status): return f"Change status to \"{status}\""

# Shop stats
registration_stats = "👥 Registration statistics"
order_stats = "📦 Order statistics"
all_time = "All time"
monthly = "Last 30 days"
weekly = "Last 7 days"
daily = "Last 24 hours"

# Payment settings
yoomoney = "🟢 YooMoney"
qiwi = "🏧 QIWI"



# Shop settings
main_settings = "🛠️ Main settings"
item_settings = "🗃️ Item settings"
payment_settings = "💳 Payment settings"
additional_settings = "📖 Additional settings"
custom_commands = "📖 Commands"
add_command = "📝 Add command"
clean_logs = "📖 Clean logs"
clean_logs_text = "⚠️ Are you sure you want to clean the logs? They will be permanently deleted!"
backups = "💾 Backups"
update_backup = "🔄 Update backup"
load_backup = "💿 Load backup"
clean_backups = "🧹 Clean backups"
system_settings = "💻 System settings"
clean_images = "🗑️ Clean unused images"
clean_images_text = "⚠️ Are you sure you want to clean unused images? They will be permanently deleted!"
clean_database = "📚 Clean database"
clean_database_text = "⚠️ Are you sure you want to clean the database? All data will be permanently deleted!"
reset_settings = "⚙️ Reset settings"
resert_settings_text = "⚠️ Are you sure you want to reset the settings? All data will be permanently deleted!"
image = "🖼️ Image"
checkout_settings = "🛒 Checkout settings"
stats_settings = "📈 Statistics settings"
graph_color = "🌈 Graph color"
border_width = "🔲 Border width"
title_font_size = "ℹ️ Title font size"
axis_font_size = "↔️ Axis text size"
tick_font_size = "🔢 Tick text size"
unavailable = "⛔️"
minus = "➖"
plus = "➕"
enable_sticker = "❌ Enable welcome sticker"
disable_sticker = "✅ Disable welcome sticker"

toggle_email = "Email on checkout"
toggle_phone_number = "Phone number on checkout"
enable_delivery = "❌ Enable delivery"
disable_delivery = "✅ Disable delivery"
toggle_captcha = "CAPTCHA on checkout"
enable_debug = "❌ Debug mode"

input_email = f"Enter email {or_press_back}"
input_phone = f"Enter phone number {or_press_back}"
input_address = f"Enter address {or_press_back}"
input_captcha = f"Enter CAPTCHA {or_press_back}"
input_captcha_error = "Invalid CAPTCHA"
input_email_error = "Invalid email"
input_phone_error = "Invalid phone number"

input_delivery_price = f"💰 Enter delivery price {or_press_back}"
change_delivery_price = "💰 Change delivery price"
disable_debug = "✅ Debug mode disabled"

# Manager tab
view_order = "📂 View order"



