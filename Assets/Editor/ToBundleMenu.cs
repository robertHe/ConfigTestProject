using UnityEngine;
using System.Collections;
using UnityEditor;
using System.IO;

public static class ToBundleMenu
{
    [MenuItem("Build Bundle/Build bundle files", false, 55)]
    public static void BuildBUndles()
    {
        BuildLuaBundle(null, "Assets/DataConfig");

        AssetDatabase.Refresh();
        string output = string.Format("{0}/{1}", Application.streamingAssetsPath, "Android");
        BuildPipeline.BuildAssetBundles(output, BuildAssetBundleOptions.DeterministicAssetBundle, EditorUserBuildSettings.activeBuildTarget);
    }


    static void BuildLuaBundle(string subDir, string sourceDir)
    {
        string[] files = Directory.GetFiles(sourceDir + subDir, "*.bytes");
        string bundleName = subDir == null ? "lua.unity3d" : "lua" + subDir.Replace('/', '_') + ".unity3d";
        bundleName = bundleName.ToLower();

#if UNITY_5        
        for (int i = 0; i < files.Length; i++)
        {
            AssetImporter importer = AssetImporter.GetAtPath(files[i]);

            if (importer)
            {
                importer.assetBundleName = bundleName;
                importer.assetBundleVariant = null;
            }
        }
#else        
        List<Object> list = new List<Object>();

        for (int i = 0; i < files.Length; i++)
        {
            Object obj = AssetDatabase.LoadMainAssetAtPath(files[i]);
            list.Add(obj);
        }

        BuildAssetBundleOptions options = BuildAssetBundleOptions.CollectDependencies | BuildAssetBundleOptions.CompleteAssets | BuildAssetBundleOptions.DeterministicAssetBundle;

        if (files.Length > 0)
        {
            string output = string.Format("{0}/{1}/" + bundleName, Application.streamingAssetsPath, GetOS());
            File.Delete(output);
            BuildPipeline.BuildAssetBundle(null, list.ToArray(), output, options, EditorUserBuildSettings.activeBuildTarget);            
        }
#endif

        AssetDatabase.Refresh();
    }

}
