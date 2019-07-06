using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Text.RegularExpressions;

namespace RegularTools
{
    public partial class Form1 : Form
    {
        string configfile = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + "\\regulartools.json";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                if (File.Exists(configfile))
                {
                    this.Height = Convert.ToInt32(readconfig("height"));
                    this.Width = Convert.ToInt32(readconfig("width"));
                    this.Location = 
                        new Point(Convert.ToInt32(readconfig("x")), Convert.ToInt32(readconfig("y")));
                }
                else
                {
                    createconfig();
                }
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string input = richTextBox1.Text;
                string pattern = textBox1.Text;
                MatchCollection mc;
                if (checkBox2.Checked)
                {
                    mc = Regex.Matches(input, pattern, RegexOptions.IgnoreCase);
                }
                else
                {
                    mc = Regex.Matches(input, pattern);
                }
                if (checkBox1.Checked)
                {
                    richTextBox2.Text = "共找到 " + mc.Count + " 处匹配:\n";
                    foreach (Match m in mc)
                    {
                        richTextBox2.Text += m.Value + "\n";
                    }
                }
                else
                {
                    if (mc.Count != 0)
                    {
                        richTextBox2.Text = "匹配位置: 0\n" + "匹配结果: " + mc[0].Value + "\n";
                    }
                }
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                string input = richTextBox1.Text;
                string pattern = textBox1.Text;
                string replacement = textBox2.Text;
                Regex rgx = new Regex(pattern);
                string result = rgx.Replace(input, replacement);
                richTextBox3.Text = result;
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
            }
        }
        private string readconfig(string key)
        {
            try
            {
                string pattern = "(?<=\"" + key + "\":\").+?(?=\")";
                FileStream fs = new FileStream(configfile, FileMode.Open, FileAccess.Read);
                StreamReader sr = new StreamReader(fs, Encoding.UTF8);
                string result = sr.ReadToEnd();
                sr.Close();
                fs.Close();
                return Regex.Match(result, pattern).Value;
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
                return er.Message;
            }
        }
        private void writeconfig(string key, string value)
        {
            try
            {
                string pattern = "(?<=\"" + key + "\":\").+?(?=\")";
                FileStream fs = new FileStream(configfile, FileMode.Open, FileAccess.Read);
                StreamReader sr = new StreamReader(fs, Encoding.UTF8);
                string jsoncode = sr.ReadToEnd();
                sr.Close();
                fs.Close();
                Regex rgx = new Regex(pattern);
                string result = rgx.Replace(jsoncode, value);
                FileStream f = new FileStream(configfile, FileMode.Create, FileAccess.Write);
                StreamWriter sw = new StreamWriter(f, Encoding.UTF8);
                sw.Write(result);
                sw.Close();
                f.Close();
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
            }
        }
        private void createconfig()
        {
            try
            {
                //{"height":"90","width":"100","x":"90","y":"100"}
                FileStream fs = new FileStream(configfile, FileMode.Create, FileAccess.Write);
                StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);
                sw.Write("{\"height\":\"" + this.Height.ToString() + "\",\"width\":\"" + this.Width.ToString() + "\",\"x\":\"" + this.Location.X + "\",\"y\":\"" + this.Location.Y + "\"}");
                sw.Close();
                fs.Close();
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            try
            {
                writeconfig("height", this.Height.ToString());
                writeconfig("width", this.Width.ToString());
                writeconfig("x", this.Location.X.ToString());
                writeconfig("y", this.Location.Y.ToString());
            }
            catch (Exception er)
            {
                MessageBox.Show(er.Message, this.Text, MessageBoxButtons.OK);
            }
        }

        private void 复制ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Copy();
        }

        private void 粘贴ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Paste();
        }

        private void 剪切ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Cut();
        }

        private void 全选ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            richTextBox2.Copy();
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            richTextBox2.Paste();
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            richTextBox2.Cut();
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            richTextBox2.SelectAll();
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            richTextBox3.Copy();
        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            richTextBox3.Paste();
        }

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            richTextBox3.Cut();
        }

        private void toolStripMenuItem8_Click(object sender, EventArgs e)
        {
            richTextBox3.SelectAll();
        }
    }
}