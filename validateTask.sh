curl --location --request POST 'https://asia-south1-trading-session-manager.cloudfunctions.net/task' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'apiKey=887c4d60ca13f660f8143df1ddcd5060cc5190b1dfea6938e1c06052f81c016c' \
--data-urlencode 'apiSecret=490fa626ec3036aaf89b38db24f16e20665047d86e194e05ab85cc09943c9ac5' \
--data-urlencode 'email=sriharsha406@gmail.com'

# Ensure you pass correct email. We will communicate with shortlisted cadidates through this

# Output:
# {
#    isTask1Done: boolean,
#    isTask2Done: boolean,
#    clientIDsReceived: array
# }