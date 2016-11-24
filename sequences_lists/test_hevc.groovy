import static groovy.json.JsonOutput.*
import java.util.regex.Pattern

def result = []
// Conformance list updated from previous job
def seqList = new File('/home/junaid/develop/orcc/ci-server-scripts/sequences_lists/hevc')
Pattern comment = Pattern.compile("[#,].*");
int seqCounter = 1;
if (seqList.exists() && seqList.isFile()) {
    seqList.text.eachLine() { line->
			lineContent = new String(line.minus(comment))
			if(! lineContent.isEmpty() && ! lineContent.contains("10bit") && ! lineContent.contains("MAIN10") && ! lineContent.contains("Main10")) {
				result.add(new String (seqCounter+":"+line.minus(comment)))
				seqCounter++;
			}
	}
}

// Room left for any other Main profile sequences.
seqCounter = 801

if (seqList.exists() && seqList.isFile()) {
    seqList.text.eachLine() { line->
			lineContent = new String(line.minus(comment))
			if(! lineContent.isEmpty() && (lineContent.contains("10bit") || lineContent.contains("MAIN10") || lineContent.contains("Main10"))) {
				result.add(new String (seqCounter+":"+line.minus(comment)))
				seqCounter++;
			}
	}
}

println prettyPrint(toJson(result))
