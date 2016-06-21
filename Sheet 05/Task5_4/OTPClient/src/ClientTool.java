import java.io.UnsupportedEncodingException;

/**
 * Created by ronaldbrenner on 19.06.16.
 */
public class ClientTool {

    public String decodeMessage(byte[] message, byte[] otp) throws UnsupportedEncodingException {

        byte[] decodedMessage = new byte[message.length];

        for (int i = 0; i < otp.length; i++) {
            decodedMessage[i] = (byte) (message[i] ^ otp[i]);
        }
        return new String(decodedMessage, "UTF-8");
    }

    public byte[] encodeMessage(String message, byte[] otp) throws UnsupportedEncodingException {
        byte[] messageBytes = message.getBytes("UTF-8");

        if (messageBytes.length != otp.length) {
            return null;
        }

        byte [] encodedMessage = new byte[messageBytes.length];
        for (int i = 0; i < otp.length; i++) {
            encodedMessage[i] = (byte) (messageBytes[i] ^ otp[i]);
        }
        return encodedMessage;
    }
}
