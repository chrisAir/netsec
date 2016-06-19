/**
 * Created by ronaldbrenner on 19.06.16.
 */
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class OTPServer {


    static ServerSocket serverSocket;
    final static int PORT = 4242;
    static Socket clientConnection;

    public static void main(String[] args) {

        String otp = args[0];

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

                BufferedReader clientInputReader = new BufferedReader(new InputStreamReader(clientConnection.getInputStream()));
                DataOutputStream serverOutput = new DataOutputStream(clientConnection.getOutputStream());
                System.out.println("Sending message to client: " + serverMessage);
                serverOutput.writeBytes(serverTool.encodeMessage(serverMessage, otp.getBytes()) + "\n");
                serverOutput.flush();
                String clientMessage = clientInputReader.readLine();
                System.out.println("Encoded answer from client: " + clientMessage);
                String decodedMessage = serverTool.decodeMessage(clientMessage);
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

