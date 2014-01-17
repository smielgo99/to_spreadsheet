#!/usr/bin/python

__author__ = 'smielgo99@gmail.com (Susana Mielgo)'

class JiraToSpreadsheet(object):
    def __init__(self, email, password):
        """Constructor for the JiraToSpreadsheet object.

        Takes an email and password corresponding to a gmail account
        Args:
          email: [string] The e-mail address of the account to use for the sample.
          password: [string] The password corresponding to the account specified by
              the email parameter.

        Returns:
          A JiraToSpreadsheet object used to run the sample demonstrating the
          functionality of the Document List feed.
        """
 
        self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
        self.gd_client.email = email
        self.gd_client.password = password
        self.gd_client.source = 'Spreadsheets GData Sample'
        self.gd_client.ProgrammaticLogin()
        self.curr_key = ''
        self.curr_wksht_id = ''
        self.list_feed = None


        

def main():
    
    # Parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['user=', 'pw='])
    except getopt.error, msg:
        print 'python jira_to_spreadsheet.py --user [username] --pw [password] '
        sys.exit(2)

    user = ''
    pw = ''
    key = ''
    # Process options
    for option, arg in opts:
        if option == '--user':
        user = arg
        elif option == '--pw':
        pw = arg

    while not user:
        print 'NOTE: Please run these tests only with a test account.'
        user = raw_input('Please enter your username: ')
    while not pw:
        pw = getpass.getpass()
        if not pw:
        print 'Password cannot be blank.'

    try:
        sample = JiraToSpreadsheet(user, pw)
    except gdata.service.BadAuthentication:
        print 'Invalid user credentials given.'
        return

    sample.Run()

if __name__ == '__main__':
    main()
    