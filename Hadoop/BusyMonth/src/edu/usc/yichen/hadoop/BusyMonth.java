import java.io.*;
import java.lang.*;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.GenericOptionsParser;


public class BusyMonth {
	
	public static class PassengerMapper extends Mapper<Object, Text, Text, IntWritable> 
	{
		private IntWritable pasCount = new IntWritable();
		
		public void map(Object key, Text value, Mapper.Context context) 
				throws IOException, InterruptedException{
			StringTokenizer token = new StringTokenizer(value.toString(), ",");
			token.nextToken();
			String timeStr = token.nextToken();
			
			String[] timeInfo = timeStr.split(" ");
			String month = timeInfo[0].split("/")[0], year = timeInfo[0].split("/")[2];
			String terminal = token.nextToken();
			token.nextToken();
			token.nextToken();
			String count = token.nextToken();
			if (terminal.equals("Terminal 1") || terminal.equals("Terminal 2") || terminal.equals("Terminal 3")
					 || terminal.equals("Terminal 4") || terminal.equals("Terminal 5") 
					 || terminal.equals("Terminal 6") || terminal.equals("Terminal 7")
					 || terminal.equals("Terminal 8") || terminal.equals("Tom Bradley International Terminal")) {
				pasCount = new IntWritable(Integer.valueOf(count));
				context.write(new Text(String.format("%02d", Integer.valueOf(month)) + year), pasCount);
//				System.out.println(String.format("%02d", Integer.valueOf(month)) + year + "-----" + pasCount);
			}
		}
	}
	
	public static class MonthReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
		private IntWritable result = new IntWritable();
		
		public void reduce(Text key, Iterable<IntWritable> values, Mapper.Context context) 
				throws IOException, InterruptedException {
			System.out.println("=================Start Recuding=========================");
			try {
				System.out.println(key.toString());
				int sum = 0;
				for (IntWritable val : values) {
					sum += val.get();
				}
				if (sum >= 5000000) {
					result.set(sum);
					context.write(key, result);
				}
			} 
			catch (InterruptedException e) {
				// TODO: handle exception
				System.out.println("ERROR !!!!!" + e.getMessage());
			}
		}
		
	}
	
	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
		// TODO Auto-generated method stub
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length < 2) {
			System.err.println("Usage: busymonth <in> <out>");
		    System.exit(2);
		}
		Job job = Job.getInstance(conf);
		job.setJarByClass(BusyMonth.class);
		job.setMapperClass(PassengerMapper.class);
		job.setCombinerClass(MonthReducer.class);
		job.setReducerClass(MonthReducer.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		for (int i = 0; i < otherArgs.length - 1; i++) {
			FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
		}
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[otherArgs.length - 1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}

}
