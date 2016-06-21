import java.io.*;
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
        System.out.println(args[0]);
        String serverMessage;
        String clientResponse = "heres clients answer";
        ClientTool clientTool = new ClientTool();

        try {

            clientSocket = new Socket(HOST, PORT);
            //initializing streams
            InputStream serverInput = clientSocket.getInputStream();
            DataOutputStream outputStream = new DataOutputStream(clientSocket.getOutputStream());


            System.out.println("Connection to Host established");

            //reading message from Server
            byte[] data = new byte[otp.getBytes("UTF-8").length];
            int count = serverInput.read(data);
            System.out.println("Encoded Message from Server: " + new String(data, "UTF-8"));
            //decoding
            String decodedMessage = clientTool.decodeMessage(data, otp.getBytes("UTF-8"));
            System.out.println("Decoded message from Server: " + decodedMessage);

            //sending answer to Server
            System.out.println("Answering with own message: " + clientResponse);
            byte[] clientResponseByte = clientTool.encodeMessage(clientResponse, otp.getBytes());

            //
            outputStream.write(clientResponseByte);
            outputStream.flush();
            outputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }


}
