/**
 * Created by ronaldbrenner on 19.06.16.
 */
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class OTPServer {


    static ServerSocket serverSocket;
    final static int PORT = 4242;
    static Socket clientConnection;

    public static void main(String[] args) {

        String otp = args[0];
        System.out.println(args[0]);

        try {
            serverSocket = new ServerSocket(PORT);
            System.out.println("Socket initialized");
            String serverMessage = "Hello, I am the Host";
            ServerTool serverTool = new ServerTool();

            while (true) {
                clientConnection = serverSocket.accept();
                if(clientConnection.isConnected()) {
                    System.out.println("Client connected");
                }

                InputStream clientInput = clientConnection.getInputStream();
                BufferedReader clientInputReader = new BufferedReader(new InputStreamReader(clientConnection.getInputStream()));
                DataOutputStream serverOutput = new DataOutputStream(clientConnection.getOutputStream());


                System.out.println("Sending message to client: " + serverMessage);
                byte[] outputByte = serverTool.encodeMessage(serverMessage, otp.getBytes());
                System.out.println("Sending encoded message: " + new String(outputByte, "UTF-8"));
                serverOutput.write(outputByte);
                serverOutput.flush();


                //String clientMessage = clientInputReader.readLine();
                byte[] clientBytes = new byte[otp.getBytes("UTF-8").length];
                int count = clientInput.read(clientBytes);
                System.out.println("Encoded answer from client: " + new String(clientBytes, "UTF-8"));
                String decodedMessage = serverTool.decodeMessage(clientBytes, otp.getBytes("UTF-8"));
                System.out.println("Decoded answer from client: " + decodedMessage);

                serverOutput.close();
                clientInputReader.close();

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Hello, I am the OTP Server!");

    }
}

