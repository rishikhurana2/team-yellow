import java.io.*;
import java.net.*;
import edu.wpi.first.wpilibj.networktables.NetworkTable;

public class Client {
    public static void main(String[] args) throws Exception {

    System.out.println("waiting");

    Socket soc=new Socket("localhost", 3341);
    BufferedReader inFromServer = new BufferedReader(new InputStreamReader (soc.getInputStream()));
    String fromServer = null;
    NetworkTable.setClientMode();
    NetworkTable.setIPAddress("roboRIO-3341-FRC.local");
    NetworkTable table = NetworkTable.getTable("cv");
    
    try{
        while ( true ){
            System.out.println("waiting");
            fromServer = inFromServer.readLine();
            
            if(fromServer == null){
                continue;
            }

            double azimuth = 0;
            int type = -1;

            String[] parsed = fromServer.split(";");
            
            type = Integer.parseInt(parsed[0]);
            azimuth = Double.parseDouble(parsed[1]);
            
            System.out.println("type: " + type);
            System.out.println("azimuth: " + azimuth);
            
            table.putNumber("type", type);
            table.putNumber("azimuth", azimuth);
        }
    }catch(Exception e){
        e.printStackTrace();
    }finally{
        inFromServer.close();
        soc.close();
	}

    }
}
