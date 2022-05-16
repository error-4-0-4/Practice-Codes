using namespace std;

int main()
{
  string seq,org;
  getline(cin,seq);
  getline(cin,org);
  org=tolower(org);
  seq=tolower(seq);
  map<char,pair<int,int>> mapp;
  int flag=1;
  for(int i=0;i<int(seq.size());i++)
  {
    if(seq[i]!='_')
    {
    //   if(isalpha(seq[i]))
        // seq[i]=tolower(seq[i]);
      mapp[seq[i]].first+=1;
      if(mapp[seq[i]].first>1)
      {
        flag=0;
        break;
      }
      mapp[seq[i]].second=i;
    }
  }
  if(flag==0)
  {
    cout<<"New Language Error";
  }
  else
  {
    string ans="";
    for(int i=0;i<int(org.size());i++)
    {
    //   if(isalpha(org[i]))
        //  org[i]=tolower(org[i]);
      if(mapp.find(org[i])!=mapp.end())
      {
          if(ans.size()==0)
          ans+=org[i];
          else{
        int k=ans.size()-1;
        while(k>=0 and ans[k]!=' ' and mapp[ans[k]].second>mapp[org[i]].second)
          k--;
        ans=ans.substr(0,k+1)+org[i]+ans.substr(k+1,ans.size()-k-1);
      }}
      if(org[i]==' ')
        ans+=' ';
    }
    cout<<ans;
  }
  return 0;
}