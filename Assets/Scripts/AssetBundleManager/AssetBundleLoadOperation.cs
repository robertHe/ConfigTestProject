using System.Collections;
using UnityEngine;


namespace AssetBundles
{
    public abstract class AssetBundleLoadOperation:IEnumerator
    {
        public object Current
        {
            get { return null; }
        }

        public bool MoveNext()
        {
            return !IsDone();
        }

        public void Reset()
        { }

        abstract public bool Update();
        abstract public bool IsDone();
    }
    


}