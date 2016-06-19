import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * Created by ronaldbrenner on 19.06.16.
 */
public class OTPClient {

    static Socket clientSocket;
    final static int PORT = 4242;
    final static String HOST = "localhost";


    public static void main(String[] args) {
        String otp = args[0];
        System.out.println("I am the OTP Client!");
        String serverMessage;
        String clientResponse = "I am the Client";
        OTPTool otpTool = new OTPTool();

        try {

            clientSocket = new Socket(HOST, PORT);
            BufferedReader serverInput = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            DataOutputStream outputStream = new DataOutputStream(clientSocket.getOutputStream());
            System.out.println("Connection to Host established");
            serverMessage = serverInput.readLine();
            System.out.println("Encoded Message from Server: " + serverMessage);
            String decodedMessage = otpTool.decodeMessage(serverMessage, otp.getBytes());
            System.out.println("Decoded message from Server: " + decodedMessage);
            System.out.println("Answering with own message: " + clientResponse);
            outputStream.writeBytes(clientResponse);
            outputStream.flush();
            outputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }


}
