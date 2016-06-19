package otp.server;

import java.net.ServerSocket;

/**
 * Created by ronaldbrenner on 19.06.16.
 */
public class OTPServer {

    static ServerSocket serverSocket;
    final static int port = 4242;

    public static void main(String[] args) {

        System.out.println("I am a server listening to a socket");

    }
}
