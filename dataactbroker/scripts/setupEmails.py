from dataactcore.interfaces.db import GlobalDB
from dataactcore.logging import configure_logging
from dataactcore.models.userModel import EmailTemplateType, EmailTemplate
from dataactvalidator.app import createApp


def setupEmails():
    """Create email templates from model metadata."""
    with createApp().app_context():
        sess = GlobalDB.db().session

        # insert email template types
        typeList = [
            ('review_submission', '')
        ]
        for t in typeList:
            email_id = sess.query(
                EmailTemplateType.email_template_type_id).filter(
                EmailTemplateType.name == t[0]).one_or_none()
            if not email_id:
                emailType = EmailTemplateType(name=t[0], description=t[1])
                sess.add(emailType)

        sess.commit()

        # insert email templates

        #Submission Review
        template = "[REV_USER_NAME] has shared a DATA Act broker submission with you. Click <a href='[REV_URL]'>here</a> to review their submission. For questions or comments, please email the DATA Act Broker Helpdesk (DATABroker@fiscal.treasury.gov)."
        load_email_template(sess, "DATA Act Broker - Submission Ready for Review", template, "review_submission")


def load_email_template(sess, subject, contents, email_type):
    """ Upsert a broker e-mail template.

    Args:
        sess - Database session
        subject - Subject line
        contents - Body of email, can include tags to be replaced
        email_type - Type of template, if there is already an entry for this type it will be overwritten
    """
    email_id = sess.query(
        EmailTemplateType.email_template_type_id).filter(
        EmailTemplateType.name == email_type).one()
    template_id = sess.query(
        EmailTemplate.email_template_id).filter(
        EmailTemplate.template_type_id == email_id).one_or_none()
    template = EmailTemplate()
    if template_id:
        template.email_template_id = template_id
    template.subject = subject
    template.content = contents
    template.template_type_id = email_id
    sess.merge(template)
    sess.commit()

if __name__ == '__main__':
    configure_logging()
    setupEmails()
