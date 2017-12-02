import java.io.*;
import java.net.*;
import edu.wpi.first.wpilibj.networktables.NetworkTable;
public class client {
    public static void main(String[] args) throws Exception {

      System.out.println("waiting");

    Socket soc=new Socket("localhost", 3341);
    BufferedReader inFromServer = new BufferedReader(new InputStreamReader (soc.getInputStream()));
    String fromServer = null;
    NetworkTable.setClientMode();
    NetworkTable.setIPAddress("roboRIO-3341-FRC.local");
    NetworkTable table = NetworkTable.getTable("cv");
    try{
    while ( true )
    {
        System.out.println("waiting");
        fromServer = inFromServer.readLine();
        if(fromServer == null){

          continue;
        }
        double distance = 0, azimuth = 0, altitude = 0;
        String orientation = "";

        String[] parsed = fromServer.split(";");
        distance = Double.parseDouble(parsed[0]);
        azimuth = Double.parseDouble(parsed[1]);
        altitude = Double.parseDouble(parsed[2]);
        orientation = parsed[3];
        System.out.println("distance: " + distance);
        System.out.println("azimuth: " + azimuth);
        System.out.println("altitude: " + altitude);
        System.out.println("orientation: " + orientation);
        table.putString("orientation", orientation);
        table.putNumber("gearDistance", distance);
        table.putNumber("gearAzimuth", azimuth);
				table.putNumber("gearAltitude", altitude);

    }
    }
    catch(Exception e){
        e.printStackTrace();
      }
    finally
		{
      inFromServer.close();
      soc.close();
		}

    }
  }
