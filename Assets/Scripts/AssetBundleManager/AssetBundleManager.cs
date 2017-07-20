using UnityEngine;
using System.Collections;
using System;

namespace AssetBundles
{

    /// <summary>
    /// Loaded assetbundle contains the references count which can be used to
    /// unload dependent assetbundles automaticlly
    /// </summary>
    public class LoadedAssetBundle
    {
        public AssetBundle mAssetBundle;
        public int mReferencedCount;

        internal event Action unload;

        internal void OnUnload()
        {
            mAssetBundle.Unload(false);
            if (unload != null)
                unload();
        }
        
        public LoadedAssetBundle(AssetBundle assetbundle)
        {
            mAssetBundle = assetbundle;
            mReferencedCount = 1;
        }
    }


    /// <summary>
    /// Class takes care of loading assetbundles and its depedencies
    /// automatically, loading variants automatically
    /// </summary>
    public class AssetBundleManager : MonoBehaviour
    {


    }

}
