use std::collections::HashMap;

fn counter(dict:&mut HashMap<String, u32>, key:String){
    let count = dict.entry(key.to_lowercase()).or_insert(0);
    *count += 1;
}

fn get_key_by_max_value(dict: HashMap<String, u32>) -> String {
    let mut max:u32 = 0;
    let mut key = String::from("");
    for item in dict {
        if item.1 > max {
            max = item.1;
            key = item.0;
        }
    }
    return key
}

impl Solution {
    pub fn most_common_word(paragraph: String, banned: Vec<String>) -> String {
        let mut dict:HashMap<String, u32> = HashMap::new();
        let mut key:String = String::from("");
        for c in paragraph.to_lowercase().chars() {
            if c.is_alphabetic() {
                let s = c.to_string();
                key.push_str(&s);
                continue
            }
            if (key == ""){
                continue
            }
            if (banned.contains(&key)){
                key = String::from("");
                continue
            }
            counter(&mut dict, key.to_string());
            key = String::from("");
        }
        if key != "" {
            counter(&mut dict, key.to_string());
        }
        get_key_by_max_value(dict)
    }
}