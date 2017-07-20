using UnityEngine;
using System.Collections;
using System.IO;
using ProtoBuf;
using xlsc.battle_gold;
using xlsc.language;
using xlsc.goods;

public class ReadProtoBytes : MonoBehaviour
{
    void Start()
    {
        float time = Time.realtimeSinceStartup;
        GOODS_CONF_ARRAY goods = ReadOneDataConfig<GOODS_CONF_ARRAY>("xlsc_goods_goods_conf");
        Debug.Log("time = " + (Time.realtimeSinceStartup-time));
    }

    private T ReadOneDataConfig<T>(string FileName)
    {
        FileStream fileStream;
        fileStream = GetDataFileStream(FileName);
        if (null != fileStream)
        {
            T t = Serializer.Deserialize<T>(fileStream);
            fileStream.Close();
            return t;
        }

        return default(T);
    }
    private FileStream GetDataFileStream(string fileName)
    {
        string filePath = GetDataConfigPath(fileName);
        if (File.Exists(filePath))
        {
            FileStream fileStream = new FileStream(filePath, FileMode.Open);
            return fileStream;
        }

        return null;
    }
    private string GetDataConfigPath(string fileName)
    {
        return Application.streamingAssetsPath + "/DataConfig/" + fileName + ".bytes";
    }
}
