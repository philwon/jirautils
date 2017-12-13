# jirautils

To export baseline issues, use following command:

./exportBaselineIssue.py -u username -p password

To export outsource issues, use following command:

./exportNoneSWIssue.py -u username -p password

To export CVP issues, use following command:
./exportCVPIssue.py -u username -p password -a assignee

These three py scripts only process ToDo and Doing issue, you can modify it by yourself.

The razor.jar is used to import issue to jira. See help of the jar file by:
java -jar razor.jar
