#!/bin/bash  
  
# 遍历该文件夹下的所有文件  
for file in *; do  
    # 跳过非普通文件（如目录、链接等）  
    if [[ ! -f "$file" || "$file" == "rename.sh" ]]; then  
        continue  
    fi  
  
    # 提取文件的后缀（如果有的话）  
    extension="${file##*.}"  
    # 如果文件没有后缀，则默认为空字符串  
    if [[ -z "$extension" ]]; then  
        extension=""  
    fi  
  
    # 获取文件的修改时间，并格式化为YYYY-MM-DD_HH-MM-SS的形式  
    timestamp=$(date -r "$file" +%Y-%m-%d_%H-%M-%S)  
  
    # 构建新的文件名  
    new_file="file_${timestamp}.$extension"  
  
    # 如果新文件名已经存在，则添加后缀以避免冲突（例如：_1, _2, ...）  
    counter=1  
    while [[ -e "$new_file" ]]; do  
        new_file="file_${timestamp}_${counter}.$extension"  
        ((counter++))  
    done  
  
    # 执行重命名操作  
    mv "$file" "$new_file"  
done  
  
echo "所有文件已重命名完成。"
