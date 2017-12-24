import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class BusyMonth {
    
    public static class TokenizerMapper
        extends Mapper<Object, Text, Text, IntWritable>{
            private IntWritable pasCount = new IntWritable();
            //private Text word = new Text();
            
            public void map(Object key, Text value, Context context) 
                    throws IOException, InterruptedException{
                StringTokenizer token = new StringTokenizer(value.toString(),",");
                token.nextToken();
                String timeStr = token.nextToken();
                String[] timeInfo = timeStr.split(" ");
                String month = timeInfo[0].split("/")[0], year = timeInfo[0].split("/")[2];
                String terminal = token.nextToken();
                token.nextToken();
                token.nextToken();
                String count = token.nextToken();
                pasCount = new IntWritable(Integer.parseInt(count));
                if (terminal.equals("Terminal 1") || terminal.equals("Terminal 2") || terminal.equals("Terminal 3")
                     || terminal.equals("Terminal 4") || terminal.equals("Terminal 5") 
                     || terminal.equals("Terminal 6") || terminal.equals("Terminal 7")
                     || terminal.equals("Terminal 8") || terminal.equals("Tom Bradley International Terminal")) {
                pasCount = new IntWritable(Integer.valueOf(count));
                context.write(new Text(String.format("%02d", Integer.valueOf(month)) + "/" + year), pasCount);
//              System.out.println(String.format("%02d", Integer.valueOf(month)) + year + "-----" + pasCount);
            }
            }
    }

    public static class IntSumReducer
            extends Reducer<Text, IntWritable, Text, IntWritable>{
        private IntWritable result = new IntWritable();
            
        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException{
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
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception{
        // TODO code application logic here
        
        Configuration conf = new Configuration();
        
        Job job = Job.getInstance(conf);
        job.setJarByClass(BusyMonth.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
    
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true)?0:1);
            
      
        
    }
   
}
