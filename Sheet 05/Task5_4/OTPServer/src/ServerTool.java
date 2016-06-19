import java.io.UnsupportedEncodingException;

/**
 * Created by ronaldbrenner on 19.06.16.
 */
public class ServerTool {

    //TODO: implement decoding
    public String decodeMessage(String encodedMessage) {
        return encodedMessage;
    }

    //TODO: implement encoding
    public String encodeMessage(String message, byte[] otp) throws UnsupportedEncodingException {

        byte[] messageBytes = message.getBytes("UTF-8");

        if (messageBytes.length != otp.length) {
            return "Bad OTP Length";
        }

        byte[] encodedMessage = new byte[messageBytes.length];
        for (int i = 0; i < otp.length; i++) {
            encodedMessage[i] = (byte) (messageBytes[i] ^ otp[i]);
        }
        String encodedString = new String(encodedMessage, "UTF-8");
        return encodedString;





//        System.out.println("Message length: " + message.length());
//        byte[] messageBytes = message.getBytes("UTF-8");
//        System.out.println("bytes length: " + messageBytes.length);
//        String translatedMessage = new String(messageBytes, "UTF-8");
//        return translatedMessage;
    }
}
