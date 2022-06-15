from independentsoft.msg import Message
from independentsoft.msg import Recipient
from independentsoft.msg import ObjectType
from independentsoft.msg import DisplayType
from independentsoft.msg import RecipientType
from independentsoft.msg import MessageFlag
from independentsoft.msg import StoreSupportMask

message = Message()

recipient1 = Recipient()
recipient1.address_type = "SMTP"
recipient1.display_type = DisplayType.MAIL_USER
recipient1.object_type = ObjectType.MAIL_USER
recipient1.display_name = "John Smith"
recipient1.email_address = "John@domain.com"
recipient1.recipient_type = RecipientType.TO

recipient2 = Recipient()
recipient2.address_type = "SMTP"
recipient2.display_type = DisplayType.MAIL_USER
recipient2.object_type = ObjectType.MAIL_USER
recipient2.display_name = "Mary Smith"
recipient2.email_address = "Mary@domain.com"
recipient2.recipient_type = RecipientType.CC

message.subject = "Test"
message.body = "Body text"
message.display_to = "John Smith"
message.display_cc = "Mary Smith"
message.recipients.append(recipient1)
message.recipients.append(recipient2)
message.message_flags.append(MessageFlag.UNSENT)
message.store_support_masks.append(StoreSupportMask.CREATE)

message.save("e:\\message.msg")