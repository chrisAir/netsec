import java.io.UnsupportedEncodingException;

/**
 * Created by ronaldbrenner on 19.06.16.
 */
public class OTPTool {

    //TODO: implement decoding
    public String decodeMessage(String encodedMessage, byte[] otp) throws UnsupportedEncodingException {

        byte[] encodedBytes = encodedMessage.getBytes("UTF-8");
        byte[] decodedMessage = new byte[encodedBytes.length];

        for (int i = 0; i < otp.length; i++) {
            decodedMessage[i] = (byte) (encodedBytes[i] ^ otp[i]);
        }
        return new String(decodedMessage, "UTF-8");
    }

    public String encodeMessage(String message) {
        return message;
    }
}
