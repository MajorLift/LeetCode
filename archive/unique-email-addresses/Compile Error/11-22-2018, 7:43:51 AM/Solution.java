// https://leetcode.com/problems/unique-email-addresses

class Solution {
    
    public String[] parsedEmails(String[] input) {
        String[] Parsed = new String[input.length];
        for(String address : input) {
            int atSignIdx = address.indexOf('@');
            String localName = address.substring(0, atSignIdx-1);
            String domainName = address.substring(atSignIdx+1);

            String parsedLocalName = localName;
            int shiftCount = 0;
            for(int i=0; i<localName.length(); ++i) {
                if(localName.charAt(i) == '+') {
                    parsedLocalName = parsedLocalName.substring(0, i-shiftCount-1);
                    break;
                } if(localName.charAt(i) == '.') {
                    String heads = parsedLocalName.substring(0, i-shiftCount-1);
                    String tails = parsedLocalName.substring(i-shiftCount+1);
                    parsedLocalName = heads.concat(tails);
                    shiftCount++;
                }
            }
            String parsedAddress = parsedLocalName.concat("@");
            parsedAddress = parsedAddress.concat(domainName);
            Parsed.append(parsedAddress);
        }
        return Parsed;
    }
    
    public int numUniqueEmails(String[] emails) {
        String[] parsedEmails = parsedEmails(emails);
        int count = 0;
        for(int j=0; j<parsedEmails.length()-1; ++j) {
            String[] subarray = parsedEmails.substring(j+1);
            cmpEmail = parsedEmails[j];
            for(int i=0; i<subarray.length(); ++i) {
                if(cmpEmail == subarray[i]) count++;
            }
        }
        return emails.length() - count;
    }
}