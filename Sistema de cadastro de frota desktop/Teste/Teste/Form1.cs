using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace Teste
{
    public partial class Form1 : Form
        //conexao
    {
        SqlConnection con = new SqlConnection("Data Source=LAPTOP-D85AFCNH\\SQLEXPRESS;Initial Catalog=Sistema;Integrated Security=True");
        SqlCommand comando = new SqlCommand();
        SqlDataReader dr;
        public Form1()
        {
            comando.Connection = con;
            InitializeComponent();
            carregarLista();
        }

        private void button1_Click(object sender, EventArgs e)
            //insert
        {
            if (textBox1.Text != "" & textBox2.Text != "")
            {
                con.Open();
                comando.CommandText = "INSERT INTO tbVeiculo(Nome,placa) VALUES('" + textBox1.Text + "','" + textBox2.Text + "')";
                comando.ExecuteNonQuery();
                con.Close();

                carregarLista();

                textBox1.Text = "";
                textBox2.Text = "";
            }
        }
        private void carregarLista()
            //load list
        {
            listBox1.Items.Clear();
            listBox2.Items.Clear();

            con.Open();
            comando.CommandText = "SELECT * FROM tbVeiculo";
            dr = comando.ExecuteReader();
            if (dr.HasRows)
            {
                while (dr.Read())
                {
                    listBox1.Items.Add(dr[1].ToString());
                    listBox2.Items.Add(dr[2].ToString());
                }
            }
            con.Close();
        }

        private void listBox2_SelectedIndexChanged(object sender, EventArgs e)
            //load list 2
        {
            ListBox l = sender as ListBox;
            if (l.SelectedIndex != -1)
            {
                listBox1.SelectedIndex = l.SelectedIndex;
                listBox2.SelectedIndex = l.SelectedIndex;

                textBox1.Text = listBox1.SelectedItem.ToString();
                textBox2.Text = listBox2.SelectedItem.ToString();
            }
        }

        private void button2_Click(object sender, EventArgs e)
            //delet
        {
            if (textBox1.Text != "" & textBox2.Text != "")
            {
                con.Open();
                comando.CommandText = "DELETE FROM tbVeiculo WHERE Nome ='" + textBox1.Text + "'AND Placa= '" + textBox2.Text + "'";
                comando.ExecuteNonQuery();
                con.Close();

                carregarLista();

                textBox1.Text = "";
                textBox2.Text = "";

            }
        }

        private void button3_Click(object sender, EventArgs e)
            //update 
        {
            if (textBox1.Text != "" & textBox2.Text != "")
            {
                con.Open();
                comando.CommandText = "UPDATE tbVeiculo SET Nome='"+textBox1.Text+"', Placa='"+textBox2.Text+"' WHERE Placa='"+listBox2.SelectedItem.ToString()+"' AND Nome='"+listBox1.SelectedItem.ToString()+"'";
                comando.ExecuteNonQuery();
                con.Close();

                carregarLista();

                textBox1.Text = "";
                textBox2.Text = "";

            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int i;
            i = 0;
            int l;
            l = 8;
            try
            {
                if(SqlConnection == con.Open)
                {

                }
            }
            catch
            {

            }
            for(i=0;i<l; i++)
            {
                comando.CommandText = "SELECT * FROM tbVeiculo WHERE codigo = i";
            }
        }

        private void menuPrincipalToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Menu men = new Menu();
            men.Show();
        }
    }
}
