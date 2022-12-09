package threadpracticeprogram;

public class ThreadSample extends Thread
{ 
	public void run()
	{ 
		for(int i=0;i<10;i++)
		{
			System.out.println("first thread program hello  hello pytho pro");
		}
	
     }
}
	
 class SampleTwo extends ThreadSample 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		ThreadSample t=new ThreadSample();
		t.start();
	}

}


