use std::cmp::Ordering;
struct Log {
    id: String,
    value: String,
    origin: String,
}

impl Log{
    fn cmp(&self, other: &Self) -> Ordering {
        if self.value == other.value {
            return self.id.cmp(&other.id)
        }
        return self.value.cmp(&other.value)
    }
}

fn is_numeric(s:&String) -> bool{
    for c in s.chars() {
        if c == ' ' {
            continue
        }
        if !c.is_numeric() {
            return false
        }
    }
    return true
}


impl Solution {
    pub fn reorder_log_files(logs: Vec<String>) -> Vec<String> {
        let mut letter_logs:Vec<Log> = vec![];
        let mut digit_logs:Vec<String> = vec![];
        for log in logs {
            let i = log.find(" ");
            let id = log[0..i.unwrap()].to_string();
            let value = log[i.unwrap()..].to_string();
            if is_numeric(&value) {
                digit_logs.push(log);
            } else {
                letter_logs.push(Log{id,value, origin:log})
            }
        };
        letter_logs.sort_by(|a, b| a.cmp(b));
        let mut letter_logs_2:Vec<String> = vec![];
        for log in letter_logs {
            letter_logs_2.push(log.origin);
        }
        letter_logs_2.append(&mut digit_logs);
        return letter_logs_2
    }
}