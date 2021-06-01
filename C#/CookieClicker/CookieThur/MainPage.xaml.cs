using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace CookieThur
{
    public partial class MainPage : ContentPage
    {
        int autoClickerLevel = 0;
        public MainPage()
        {
            InitializeComponent();
            var t = new Task(() =>
            {
                while (true)
                {
                    DateTime start = DateTime.Now;
                    while ((DateTime.Now - start).TotalSeconds < 1)
                    {
                        //do nothing
                    }
                    cookies = cookies + autoClickerLevel * cookiesPerClick;
                    Device.BeginInvokeOnMainThread(() =>
                    {
                        CookieLabel.Text = cookies.ToString();
                    });
                }
            });
            t.Start();
        }

        int cookies = 0;
        int cookiesPerClick = 1;

        void CookieClicked(System.Object sender, System.EventArgs e)
        {
            cookies = cookies + cookiesPerClick;
            CookieLabel.Text = cookies.ToString();
        }

        void UpgradeClicked(System.Object sender, System.EventArgs e)
        {
            if (cookies >= 5 * cookiesPerClick)
            {
                cookies = cookies - 5 * cookiesPerClick;
                cookiesPerClick = cookiesPerClick + 1;
                CookieLabel.Text = cookies.ToString();
                UpgradeButton.Text = "Upgrade (" + (5 * cookiesPerClick).ToString() + ")";
            }
        }

        void Button_Clicked(System.Object sender, System.EventArgs e)
        {
            autoClickerLevel += 1;
        }
    }
}
